
# Parameters

    Name :                      ReTest18-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      55221424814 function calls (54979020491 primitive calls) in 86112.98 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.981 86112.981 {built-in method builtins.exec}
                      1    8.738    8.738 86112.981 86112.981 <string>:1(<module>)
                      1  586.611  586.611 86104.243 86104.243 main.py:75(CFagent)
                9055851   62.176    0.000 27970.615    0.003 agent.py:29(learn)
                9053015  772.975    0.000 21902.090    0.002 learner.py:42(Qlearn)
                3018617   20.899    0.000 20201.930    0.007 game.py:41(step)
                3018617   26.512    0.000 19337.767    0.006 layers.py:718(step)
                3018617  343.514    0.000 13134.949    0.004 layers.py:17(step)
              300270278 1197.789    0.000 12763.709    0.000 layer.py:98(move)
        272662072/30259440 1378.596    0.000 11448.314    0.000 module.py:866(_call_impl)
                3018617  580.236    0.000 10881.977    0.004 agent.py:54(_learn)
               21206425   85.727    0.000 10518.033    0.000 network.py:24(forward)
               21206425  360.698    0.000 10245.218    0.000 container.py:117(forward)
                3018617  578.242    0.000 9858.243    0.003 agent.py:202(_learn)
                3018617 6757.998    0.002 8468.639    0.003 replaybuffer.py:22(sample_data)
                3018617 6403.696    0.002 8054.533    0.003 replaybuffer.py:52(sample_data)
                9053015  126.770    0.000 7961.488    0.001 optimizer.py:84(wrapper)
              300270278 1162.511    0.000 7671.471    0.000 layers.py:735(check)
                9053015   65.976    0.000 7427.975    0.001 grad_mode.py:24(decorate_context)
                9053015  377.259    0.000 7212.435    0.001 adam.py:55(step)
                3018617  159.200    0.000 7139.755    0.002 agent.py:117(_learn)
                9053015 1527.165    0.000 6465.485    0.001 _functional.py:53(adam)
                3018618  506.020    0.000 6130.759    0.002 layers.py:684(update)
                9053015   58.121    0.000 6053.751    0.001 tensor.py:195(backward)
                9053015   67.017    0.000 5994.148    0.001 __init__.py:68(backward)
                9053015 5657.165    0.001 5657.165    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3018617  843.010    0.000 5602.004    0.002 agent.py:210(counterfact)
                6073718  312.035    0.000 5325.649    0.001 agent.py:49(__call__)
                3018617 1849.576    0.001 4355.806    0.001 agent.py:88(interveen)
               42260645 2424.099    0.000 4107.888    0.000 layer.py:151(update)
               42412850  117.682    0.000 3953.010    0.000 conv.py:398(forward)
               42412850   96.697    0.000 3776.683    0.000 conv.py:390(_conv_forward)
                3018617 2265.473    0.001 3718.114    0.001 replaybuffer.py:28(teleporter_save_data)
               42412850 3679.986    0.000 3679.986    0.000 {built-in method conv2d}
               38719819 3518.618    0.000 3518.618    0.000 {built-in method tensor}
               31742247   25.351    0.000 3292.520    0.000 game.py:37(board)
              300270278  455.795    0.000 3050.331    0.000 layers.py:729(isFree)
               57582041  136.631    0.000 2889.495    0.000 linear.py:93(forward)
               39264325 2811.273    0.000 2811.273    0.000 {built-in method cat}
                3018617 1731.556    0.001 2769.905    0.001 agent.py:67(modify)
               57582041   57.842    0.000 2676.480    0.000 functional.py:1737(linear)
               57582041 2605.705    0.000 2605.705    0.000 {built-in method torch._C._nn.linear}
             1891322943 2286.501    0.000 2594.536    0.000 layer.py:95(isFree)
              300270278 1738.067    0.000 2394.246    0.000 layers.py:471(check)
              300270278 1555.484    0.000 2073.791    0.000 layers.py:77(check)
                3015781   97.204    0.000 1851.303    0.001 agent.py:171(__call__)
                9092335   93.228    0.000 1613.126    0.000 agent.py:59(modify_board)
                3018617   91.277    0.000 1554.308    0.001 agent.py:112(__call__)
                3018617 1194.787    0.000 1529.263    0.001 replaybuffer.py:58(CF_save_data)
              141556624 1504.619    0.000 1504.619    0.000 {built-in method clone}
               78788466   90.855    0.000 1468.906    0.000 activation.py:713(forward)
                1502355   25.474    0.000 1443.710    0.001 layers.py:740(restart)
                3018617   96.126    0.000 1405.630    0.000 replaybuffer.py:18(stacker)
               78788466   86.227    0.000 1378.052    0.000 functional.py:1364(leaky_relu)
                3015781   87.916    0.000 1358.968    0.000 replaybuffer.py:48(stacker)
             5093603778  934.107    0.000 1342.397    0.000 enum.py:646(__hash__)
               78788466 1278.686    0.000 1278.686    0.000 {built-in method torch._C._nn.leaky_relu}
                1502355   11.575    0.000 1246.193    0.001 level.py:8(__init__)
              168985832 1240.298    0.000 1240.298    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1502355   75.319    0.000 1127.346    0.001 levels.py:262(generate)
                9053015  212.674    0.000 1119.280    0.000 optimizer.py:189(zero_grad)
              861358429 1095.565    0.000 1095.565    0.000 layer.py:146(elements)
              168985832 1075.578    0.000 1075.578    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              303378063  251.508    0.000 1069.034    0.000 {built-in method builtins.any}
                9092335 1067.919    0.000 1067.919    0.000 {built-in method torch._C._nn.one_hot}
              300270278  815.761    0.000 1005.851    0.000 layers.py:62(check)
               17093372  163.111    0.000  984.992    0.000 level.py:41(notUsed)
             2402875560  675.467    0.000  817.525    0.000 layers.py:700(<genexpr>)
              301861800  127.408    0.000  746.806    0.000 {built-in method builtins.all}
               84492916  726.470    0.000  726.470    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               84492916  668.014    0.000  668.014    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1347620974  369.085    0.000  660.144    0.000 layers.py:690(<genexpr>)
             6626989533  635.743    0.000  635.743    0.000 layer.py:91(positions)
               84492916  607.843    0.000  607.843    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               84492916  587.523    0.000  587.523    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6037234  236.378    0.000  583.546    0.000 random.py:315(sample)
                9053015   24.557    0.000  582.602    0.000 loss.py:527(forward)
                6073718  198.056    0.000  564.483    0.000 exploration.py:53(softmaxer)
                9053015   66.248    0.000  558.045    0.000 functional.py:2898(mse_loss)
              591450496  434.194    0.000  542.229    0.000 tensor.py:906(grad)
        6005696764/6005696761  439.921    0.000  512.907    0.000 {built-in method builtins.len}
                3018617  295.096    0.000  506.816    0.000 collector.py:46(collect)
                3018617   88.745    0.000  504.449    0.000 agent.py:277(counterfact_check)
              300270278  315.466    0.000  454.476    0.000 layers.py:48(check)
               17093372   17.991    0.000  433.432    0.000 level.py:38(elementsIn)
               84492916  426.152    0.000  426.152    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5093638193  408.297    0.000  408.297    0.000 {built-in method builtins.hash}
              303214826  248.888    0.000  365.328    0.000 layer.py:126(remove)
              300270278  234.374    0.000  341.266    0.000 layers.py:23(check)
              153664740  332.630    0.000  332.630    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9053015  319.116    0.000  319.116    0.000 {built-in method torch._C._nn.mse_loss}
                9053923  305.187    0.000  305.187    0.000 {built-in method max}
               17093372  138.257    0.000  274.761    0.000 level.py:39(<listcomp>)
              388680236  199.102    0.000  273.267    0.000 layer.py:130(add)
               21130319  270.920    0.000  270.920    0.000 {built-in method sum}
                6037236  269.781    0.000  269.781    0.000 {built-in method nonzero}
              770236538  258.284    0.000  258.284    0.000 level.py:32(inverse)
                9053015   64.319    0.000  256.563    0.000 __init__.py:28(_make_grads)
               42412850   43.412    0.000  242.989    0.000 flatten.py:39(forward)
               18106030   59.293    0.000  241.959    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9515525: <ReTest18_0> in cluster <dcc> Done

Job <ReTest18_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 14 15:03:59 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 15 14:38:56 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 15 14:38:56 2021
Terminated at Fri Apr 16 14:34:15 2021
Results reported at Fri Apr 16 14:34:15 2021

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

    CPU time :                                   85912.84 sec.
    Max Memory :                                 9140 MB
    Average Memory :                             6288.84 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7244.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            171016 sec.

The output (if any) is above this job summary.

