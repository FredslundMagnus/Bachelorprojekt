
# Parameters

    Name :                      Causal3_Conver1-1
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61253736963 function calls (60934274780 primitive calls) in 86113.53 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.534 86113.534 {built-in method builtins.exec}
                      1    4.223    4.223 86113.534 86113.534 <string>:1(<module>)
                      1  358.437  358.437 86109.311 86109.311 main.py:79(CFagent)
                9813828   36.052    0.000 29444.047    0.003 agent.py:29(learn)
                9813820  731.816    0.000 24531.046    0.002 learner.py:42(Qlearn)
                3271276   15.990    0.000 16418.332    0.005 game.py:41(step)
                3271276   19.220    0.000 15663.344    0.005 layers.py:718(step)
        356986445/37525953 1462.454    0.000 13221.489    0.000 module.py:866(_call_impl)
               27712133   78.715    0.000 12425.631    0.000 network.py:27(forward)
               27712133  383.359    0.000 12175.833    0.000 container.py:117(forward)
                3271276  339.219    0.000 11361.309    0.003 agent.py:54(_learn)
                3271276 1402.648    0.000 10529.882    0.003 agent.py:212(counterfact)
                3271276  337.754    0.000 10526.083    0.003 agent.py:204(_learn)
                9813820   90.042    0.000 10370.307    0.001 optimizer.py:84(wrapper)
                9813820   40.327    0.000 9959.940    0.001 grad_mode.py:24(decorate_context)
                9813820  291.881    0.000 9825.481    0.001 adam.py:55(step)
                3271276  273.964    0.000 9390.408    0.003 layers.py:17(step)
                9813820 2017.160    0.000 9212.602    0.001 _functional.py:53(adam)
              326982171  537.275    0.000 9088.222    0.000 layer.py:98(move)
                3271276   98.334    0.000 7499.277    0.002 agent.py:117(_learn)
                8947397  239.965    0.000 6485.531    0.001 agent.py:49(__call__)
                3271277  462.202    0.000 6227.270    0.002 layers.py:684(update)
                9813820   40.024    0.000 6123.100    0.001 tensor.py:195(backward)
                9813820   41.538    0.000 6081.620    0.001 __init__.py:68(backward)
                3271276 3205.882    0.001 5964.131    0.002 replaybuffer.py:28(teleporter_save_data)
                9813820 5819.090    0.001 5819.090    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              326982171 1172.183    0.000 5396.708    0.000 layers.py:735(check)
                3271276 2988.227    0.001 5356.486    0.002 agent.py:88(interveen)
                3271276 4191.707    0.001 5257.163    0.002 replaybuffer.py:22(sample_data)
                3271276 4006.566    0.001 5043.186    0.002 replaybuffer.py:67(sample_data)
               48742599 4462.041    0.000 4462.041    0.000 {built-in method tensor}
               55424266  124.247    0.000 4367.254    0.000 conv.py:398(forward)
               41208143   31.249    0.000 4247.344    0.000 game.py:37(board)
               55424266   75.535    0.000 4187.286    0.000 conv.py:390(_conv_forward)
               55424266 4111.751    0.000 4111.751    0.000 {built-in method conv2d}
               76593847  159.297    0.000 3559.337    0.000 linear.py:93(forward)
                2408372   53.211    0.000 3521.471    0.001 agent.py:176(choose_action)
               52340424 1946.679    0.000 3327.513    0.000 layer.py:167(NoRock_update)
               76593847   64.900    0.000 3322.533    0.000 functional.py:1737(linear)
               76593847 3240.710    0.000 3240.710    0.000 {built-in method torch._C._nn.linear}
                3271276 1968.908    0.001 2922.122    0.001 agent.py:67(modify)
              210305342 2702.823    0.000 2702.823    0.000 {built-in method clone}
              326982171  514.344    0.000 2681.698    0.000 layers.py:729(isFree)
             2282382383 1819.850    0.000 2167.354    0.000 layer.py:95(isFree)
                3271276 1526.080    0.000 2066.399    0.001 replaybuffer.py:73(CF_save_data)
              104305980   82.232    0.000 1970.284    0.000 activation.py:713(forward)
              183191296 1897.703    0.000 1897.703    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              104305980   88.053    0.000 1888.052    0.000 functional.py:1364(leaky_relu)
               44931393 1852.703    0.000 1852.703    0.000 {built-in method cat}
                6087017   57.975    0.000 1838.451    0.000 layers.py:740(restart)
              104305980 1780.619    0.000 1780.619    0.000 {built-in method torch._C._nn.leaky_relu}
               12218673   81.982    0.000 1769.477    0.000 agent.py:59(modify_board)
                3271268   57.266    0.000 1657.136    0.001 agent.py:172(__call__)
              183191296 1649.657    0.000 1649.657    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3271276   55.760    0.000 1548.624    0.000 agent.py:112(__call__)
                9813820  229.152    0.000 1436.389    0.000 optimizer.py:189(zero_grad)
             5274781025  921.722    0.000 1349.516    0.000 enum.py:646(__hash__)
                6087017   29.212    0.000 1296.861    0.000 level.py:8(__init__)
              324311960  274.579    0.000 1166.232    0.000 {built-in method builtins.any}
              326982171  729.099    0.000 1148.934    0.000 layers.py:246(check)
               12218673 1125.457    0.000 1125.457    0.000 {built-in method torch._C._nn.one_hot}
               91595648 1032.859    0.000 1032.859    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6087017  119.926    0.000 1032.362    0.000 levels.py:164(generate)
              326982171  610.777    0.000 1021.996    0.000 layers.py:286(check)
              327127700  100.954    0.000  952.086    0.000 {built-in method builtins.all}
               91595648  893.249    0.000  893.249    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2889366147  733.438    0.000  891.652    0.000 layers.py:700(<genexpr>)
             1121137461  283.813    0.000  890.473    0.000 layers.py:690(<genexpr>)
               91595648  850.982    0.000  850.982    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91595648  844.178    0.000  844.178    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3271276   63.833    0.000  832.193    0.000 replaybuffer.py:18(stacker)
                3271268   65.103    0.000  811.136    0.000 replaybuffer.py:63(stacker)
             1324349815  791.878    0.000  791.878    0.000 layer.py:146(elements)
               12174034  105.578    0.000  752.216    0.000 level.py:41(notUsed)
              225795283  686.353    0.000  686.353    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3271276  404.270    0.000  672.581    0.000 collector.py:46(collect)
                8947397  247.386    0.000  671.716    0.000 exploration.py:53(softmaxer)
               91595648  659.951    0.000  659.951    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6381650956  574.888    0.000  574.888    0.000 layer.py:91(positions)
        7467195582/7467195579  507.087    0.000  574.232    0.000 {built-in method builtins.len}
              327127700  372.822    0.000  560.423    0.000 layers.py:113(isDone)
               18716586  213.565    0.000  558.665    0.000 random.py:315(sample)
              641169620  421.704    0.000  526.697    0.000 tensor.py:906(grad)
                2408372  524.131    0.000  524.131    0.000 agent.py:187(convert_values)
              326982171  324.028    0.000  518.577    0.000 layers.py:273(check)
              326982171  311.727    0.000  501.154    0.000 layers.py:313(check)
                9813820   14.483    0.000  480.167    0.000 loss.py:527(forward)
               48696136   57.956    0.000  467.627    0.000 layer.py:69(restart)
                9813820   36.775    0.000  465.684    0.000 functional.py:2898(mse_loss)
              326982171  292.588    0.000  438.128    0.000 layers.py:48(check)
             5274818352  427.801    0.000  427.801    0.000 {built-in method builtins.hash}
              307527622  279.383    0.000  361.448    0.000 layer.py:126(remove)
              326982171  235.813    0.000  350.545    0.000 layers.py:23(check)
               55424266   36.677    0.000  323.868    0.000 flatten.py:39(forward)
              612455938  236.395    0.000  322.020    0.000 layer.py:130(add)
                9813820  303.954    0.000  303.954    0.000 {built-in method torch._C._nn.mse_loss}
               12174034   12.808    0.000  303.022    0.000 level.py:38(elementsIn)
                6087117  150.932    0.000  298.153    0.000 layers.py:36(reset)
               55424266  287.191    0.000  287.191    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               19627656  286.992    0.000  286.992    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579155: <Causal3_Conver1_1> in cluster <dcc> Done

Job <Causal3_Conver1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:05 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 27 04:50:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 04:50:52 2021
Terminated at Wed Apr 28 04:46:12 2021
Results reported at Wed Apr 28 04:46:12 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85894.62 sec.
    Max Memory :                                 9419 MB
    Average Memory :                             6325.82 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6965.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86122 sec.
    Turnaround time :                            93727 sec.

The output (if any) is above this job summary.

