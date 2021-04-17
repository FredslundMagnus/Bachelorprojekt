
# Parameters

    Name :                      ReTest17-0
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
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65533725400 function calls (65242881425 primitive calls) in 86121.26 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.260 86121.260 {built-in method builtins.exec}
                      1    3.967    3.967 86121.260 86121.260 <string>:1(<module>)
                      1  393.030  393.030 86117.293 86117.293 main.py:75(CFagent)
               10888749   42.735    0.000 32433.674    0.003 agent.py:29(learn)
               10883957  806.970    0.000 26945.111    0.002 learner.py:42(Qlearn)
                3629583   15.989    0.000 20011.302    0.006 game.py:41(step)
                3629583   22.323    0.000 19203.010    0.005 layers.py:718(step)
                3629583  321.091    0.000 13392.466    0.004 layers.py:17(step)
              361422915 1279.760    0.000 13041.143    0.000 layer.py:98(move)
                3629583  387.556    0.000 12525.557    0.003 agent.py:54(_learn)
        327172959/36330675 1368.058    0.000 12145.112    0.000 module.py:866(_call_impl)
                3629583  385.035    0.000 11606.101    0.003 agent.py:202(_learn)
               10883957   94.594    0.000 11363.824    0.001 optimizer.py:84(wrapper)
               25446718   77.323    0.000 11306.771    0.000 network.py:24(forward)
               25446718  358.205    0.000 11065.074    0.000 container.py:117(forward)
               10883957   45.269    0.000 10921.264    0.001 grad_mode.py:24(decorate_context)
               10883957  326.347    0.000 10767.545    0.001 adam.py:55(step)
               10883957 2229.335    0.000 10087.590    0.001 _functional.py:53(adam)
                3629583  109.258    0.000 8232.670    0.002 agent.py:117(_learn)
              361422915 1291.899    0.000 8168.322    0.000 layers.py:735(check)
               10883957   45.128    0.000 6761.133    0.001 tensor.py:195(backward)
               10883957   44.171    0.000 6714.399    0.001 __init__.py:68(backward)
               10883957 6428.598    0.001 6428.598    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3629583 4577.812    0.001 5762.705    0.002 replaybuffer.py:22(sample_data)
                3629584  505.889    0.000 5756.466    0.002 layers.py:684(update)
                7273676  201.477    0.000 5318.153    0.001 agent.py:49(__call__)
                3629583  685.949    0.000 5128.129    0.001 agent.py:210(counterfact)
                3629583 3866.982    0.001 5009.974    0.001 replaybuffer.py:52(sample_data)
                3629583 2375.587    0.001 4997.665    0.001 agent.py:88(interveen)
                3629583 2448.593    0.001 4560.294    0.001 replaybuffer.py:28(teleporter_save_data)
               50893436  108.145    0.000 4000.850    0.000 conv.py:398(forward)
               50893436   68.627    0.000 3837.880    0.000 conv.py:390(_conv_forward)
               50893436 3769.253    0.000 3769.253    0.000 {built-in method conv2d}
               44496822 3638.254    0.000 3638.254    0.000 {built-in method tensor}
               36172058   23.769    0.000 3388.351    0.000 game.py:37(board)
               50814169 1978.118    0.000 3323.032    0.000 layer.py:151(update)
               69080988  142.227    0.000 3196.826    0.000 linear.py:93(forward)
                3629583 2017.509    0.001 3066.784    0.001 agent.py:67(modify)
               69080988   56.408    0.000 2985.321    0.000 functional.py:1737(linear)
               69080988 2914.470    0.000 2914.470    0.000 {built-in method torch._C._nn.linear}
              361422915  466.598    0.000 2735.475    0.000 layers.py:729(isFree)
              361422915 1960.869    0.000 2720.826    0.000 layers.py:471(check)
             2256057977 1936.782    0.000 2268.876    0.000 layer.py:95(isFree)
              361422915 1517.289    0.000 2081.948    0.000 layers.py:77(check)
              203160808 2061.926    0.000 2061.926    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              157822851 2009.260    0.000 2009.260    0.000 {built-in method clone}
               47175129 1957.312    0.000 1957.312    0.000 {built-in method cat}
                3624791   67.823    0.000 1841.629    0.001 agent.py:171(__call__)
              203160808 1801.219    0.000 1801.219    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               94527706   78.045    0.000 1761.571    0.000 activation.py:713(forward)
                3629583   64.990    0.000 1730.278    0.000 agent.py:112(__call__)
               94527706   80.523    0.000 1683.526    0.000 functional.py:1364(leaky_relu)
               10903259   78.917    0.000 1589.649    0.000 agent.py:59(modify_board)
               94527706 1586.909    0.000 1586.909    0.000 {built-in method torch._C._nn.leaky_relu}
               10883957  257.379    0.000 1571.560    0.000 optimizer.py:189(zero_grad)
             6128059552 1059.603    0.000 1520.175    0.000 enum.py:646(__hash__)
                1737850   20.607    0.000 1465.665    0.001 layers.py:740(restart)
                3629583 1099.603    0.000 1416.382    0.000 replaybuffer.py:58(CF_save_data)
                1737850   10.845    0.000 1269.322    0.001 level.py:8(__init__)
              364850134  272.603    0.000 1190.792    0.000 {built-in method builtins.any}
                1737850   78.236    0.000 1176.456    0.001 levels.py:262(generate)
              101580404 1123.749    0.000 1123.749    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               19773696  169.256    0.000 1028.516    0.000 level.py:41(notUsed)
               10903259 1016.964    0.000 1016.964    0.000 {built-in method torch._C._nn.one_hot}
              101580404  983.725    0.000  983.725    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              101580404  931.560    0.000  931.560    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              101580404  925.285    0.000  925.285    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3629583   64.800    0.000  922.719    0.000 replaybuffer.py:18(stacker)
              361422915  707.618    0.000  920.735    0.000 layers.py:62(check)
             2889764400  760.990    0.000  918.189    0.000 layers.py:700(<genexpr>)
                3624791   61.351    0.000  893.944    0.000 replaybuffer.py:48(stacker)
             1030983961  771.893    0.000  771.893    0.000 layer.py:146(elements)
                3629583  449.329    0.000  740.200    0.000 collector.py:46(collect)
              101580404  715.766    0.000  715.766    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             7697947164  686.515    0.000  686.515    0.000 layer.py:91(positions)
              362958400  126.387    0.000  637.458    0.000 {built-in method builtins.all}
              711062912  468.102    0.000  578.555    0.000 tensor.py:906(grad)
                7273676  201.955    0.000  562.581    0.000 exploration.py:53(softmaxer)
        7113672721/7113672718  487.751    0.000  558.567    0.000 {built-in method builtins.len}
             1469352281  343.744    0.000  552.680    0.000 layers.py:690(<genexpr>)
                3629583   97.907    0.000  530.814    0.000 agent.py:277(counterfact_check)
               10883957   14.910    0.000  525.630    0.000 loss.py:527(forward)
              172350901  520.679    0.000  520.679    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               10883957   44.433    0.000  510.720    0.000 functional.py:2898(mse_loss)
              361422915  341.026    0.000  508.116    0.000 layers.py:48(check)
                7259166  184.977    0.000  498.515    0.000 random.py:315(sample)
             6128100799  460.579    0.000  460.579    0.000 {built-in method builtins.hash}
               19773696   19.367    0.000  456.396    0.000 level.py:38(elementsIn)
              361422915  259.010    0.000  374.931    0.000 layers.py:23(check)
               25407081  359.102    0.000  359.102    0.000 {built-in method sum}
              365990321  228.087    0.000  338.354    0.000 layer.py:126(remove)
               10883957  333.330    0.000  333.330    0.000 {built-in method torch._C._nn.mse_loss}
               10885046  300.663    0.000  300.663    0.000 {built-in method max}
               50893436   37.438    0.000  296.951    0.000 flatten.py:39(forward)
               19773696  142.958    0.000  289.375    0.000 level.py:39(<listcomp>)
                7259168  284.720    0.000  284.720    0.000 {built-in method nonzero}
              891002983  265.068    0.000  265.068    0.000 level.py:32(inverse)
               50893436  259.512    0.000  259.512    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              464962858  189.962    0.000  254.251    0.000 layer.py:130(add)
               15558869  236.711    0.000  236.711    0.000 {method 'long' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9515524: <ReTest17_0> in cluster <dcc> Done

Job <ReTest17_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 14 15:03:59 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 15 12:08:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 15 12:08:26 2021
Terminated at Fri Apr 16 12:04:01 2021
Results reported at Fri Apr 16 12:04:01 2021

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

    CPU time :                                   85898.66 sec.
    Max Memory :                                 10318 MB
    Average Memory :                             6854.28 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6066.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86137 sec.
    Turnaround time :                            162002 sec.

The output (if any) is above this job summary.

