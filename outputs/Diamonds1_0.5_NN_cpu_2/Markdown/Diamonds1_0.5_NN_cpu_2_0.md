/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu_2-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
    Use model :                 True
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15614334577 function calls (15305212716 primitive calls) in 35700.24 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.240 35700.240 {built-in method builtins.exec}
                      1    0.001    0.001 35700.240 35700.240 <string>:1(<module>)
                      1   86.202   86.202 35700.239 35700.239 allGraphsTrain.py:13(graphTrain)
        327025274/36504524 1337.466    0.000 12529.561    0.000 module.py:715(_call_impl)
               29052075  356.580    0.000 11873.469    0.000 container.py:115(forward)
                 333751 1804.548    0.005 11385.774    0.034 allGraphs.py:156(transformNot)
                7118698   77.747    0.000 10810.849    0.002 BayesianNN.py:57(learn)
                 333751   69.204    0.000 10668.570    0.032 allGraphsTrain.py:40(<listcomp>)
                5590057   21.487    0.000 10555.345    0.002 allGraphs.py:179(getInterventionsmodel)
                7118698   86.708    0.000 10268.476    0.001 BayesianNN.py:21(learn)
               28384573   78.183    0.000 9420.001    0.000 BayesianNN.py:18(forward)
        23303065/5368660  958.564    0.000 8721.179    0.002 allGraphs.py:186(recursiveBEST)
               21265875  230.293    0.000 8517.343    0.000 BayesianNN.py:61(predict)
                7452449   45.486    0.000 4667.295    0.001 grad_mode.py:23(decorate_context)
                7452449  221.076    0.000 4531.523    0.001 adam.py:55(step)
                 333751    2.181    0.000 4468.967    0.013 agent.py:29(learn)
                 333751   52.496    0.000 4465.891    0.013 agent.py:117(_learn)
                 333751   31.021    0.000 4413.395    0.013 learner.py:42(Qlearn)
                7452449   40.738    0.000 4063.160    0.001 tensor.py:181(backward)
                7452449   27.630    0.000 4022.422    0.001 __init__.py:68(backward)
                7452449 3876.343    0.001 3876.343    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7452449  854.300    0.000 3406.920    0.000 functional.py:53(adam)
               86488723  215.484    0.000 3281.172    0.000 linear.py:92(forward)
               85153719   80.767    0.000 3201.564    0.000 dropout.py:57(forward)
               85153719  303.710    0.000 3120.797    0.000 functional.py:960(dropout)
               86488723  354.468    0.000 2975.978    0.000 functional.py:1669(linear)
                 667502    2.869    0.000 2779.895    0.004 network.py:28(forward)
               85153719 2736.504    0.000 2736.504    0.000 {built-in method dropout}
                 333751   18.975    0.000 2469.851    0.007 allGraphs.py:141(transform)
                1335004    5.378    0.000 2255.107    0.002 conv.py:422(forward)
                1335004    5.972    0.000 2247.805    0.002 conv.py:414(_conv_forward)
                1335004 2241.103    0.002 2241.103    0.002 {built-in method conv2d}
                 333751   56.502    0.000 1922.746    0.006 allGraphsTrain.py:33(<listcomp>)
               33708952  904.922    0.000 1866.250    0.000 allGraphs.py:114(states)
                 333751    2.122    0.000 1836.531    0.006 game.py:42(step)
                 333751    2.966    0.000 1793.756    0.005 layers.py:827(step)
               28384573 1290.588    0.000 1778.756    0.000 BayesianNN.py:43(convert_data)
              317675432  946.228    0.000 1594.513    0.000 tensor.py:933(grad)
              300376300 1578.070    0.000 1578.070    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               86488723 1542.880    0.000 1542.880    0.000 {built-in method addmm}
          887691/221397   53.281    0.000 1498.846    0.007 allGraphs.py:202(recursiveExplore)
                 333751    7.607    0.000 1390.814    0.004 agent.py:112(__call__)
                7452449  131.899    0.000 1168.826    0.000 optimizer.py:167(zero_grad)
               87156225   69.371    0.000 1091.427    0.000 activation.py:713(forward)
              490514124  342.900    0.000 1070.653    0.000 overrides.py:1070(has_torch_function)
               87156225  114.337    0.000 1022.055    0.000 functional.py:1292(leaky_relu)
                 333751   41.480    0.000  900.731    0.003 layers.py:17(step)
               87156225  894.730    0.000  894.730    0.000 {built-in method torch._C._nn.leaky_relu}
                 333752   63.580    0.000  885.715    0.003 layers.py:793(update)
               90764392  855.276    0.000  855.276    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              624698262  327.568    0.000  854.761    0.000 {built-in method builtins.any}
               33375100   75.357    0.000  854.578    0.000 layer.py:106(move)
               53978305  168.735    0.000  767.754    0.000 tensor.py:21(wrapped)
               86488723  654.532    0.000  654.532    0.000 {method 't' of 'torch._C._TensorBase' objects}
              340872762  563.273    0.000  563.273    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               90764392  545.074    0.000  545.074    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 333751   28.305    0.000  441.777    0.001 allGraphsTrain.py:51(<listcomp>)
                 333751   52.165    0.000  414.710    0.001 allGraphsTrain.py:44(<listcomp>)
             1108484634  332.954    0.000  407.885    0.000 overrides.py:1083(<genexpr>)
                7452449   12.474    0.000  397.175    0.000 loss.py:445(forward)
               33375100   98.803    0.000  392.599    0.000 layers.py:844(check)
                8692850  386.945    0.000  386.945    0.000 {built-in method tensor}
                7452449   47.412    0.000  384.701    0.000 functional.py:2637(mse_loss)
               56769147  366.537    0.000  366.537    0.000 {built-in method zeros}
                7258813    7.918    0.000  353.903    0.000 game.py:38(board)
                 584683    7.560    0.000  335.559    0.001 layers.py:849(restart)
               45382196  323.542    0.000  323.542    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               18934450   70.167    0.000  322.514    0.000 tensor.py:506(__rsub__)
               45382196  317.383    0.000  317.383    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5590057   51.336    0.000  311.372    0.000 allGraphs.py:167(format)
               33375100   66.235    0.000  310.117    0.000 layers.py:838(isFree)
                 584683    3.931    0.000  271.353    0.000 level.py:8(__init__)
               45382196  262.822    0.000  262.822    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               18934450  252.347    0.000  252.347    0.000 {built-in method rsub}
               35043855  244.312    0.000  244.312    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              231016280  201.171    0.000  243.882    0.000 layer.py:103(isFree)
                 333751   87.880    0.000  240.004    0.001 agent.py:67(modify)
                 584683    9.468    0.000  235.222    0.000 levels.py:151(generate)
              328026527  234.434    0.000  234.434    0.000 {built-in method torch._C._get_tracing_state}
               45382196  233.095    0.000  233.095    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7452449  218.458    0.000  218.458    0.000 {built-in method torch._C._nn.mse_loss}
                2806905   38.135    0.000  215.660    0.000 level.py:41(notUsed)
                2336264  118.704    0.000  207.420    0.000 layer.py:175(NoRock_update)
               33375100  195.040    0.000  195.040    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              517738808  134.158    0.000  193.684    0.000 enum.py:646(__hash__)
               37837112  192.375    0.000  192.375    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               63094677  191.715    0.000  191.715    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1001253    5.131    0.000  181.435    0.000 tensor.py:576(__iter__)
               87353505   41.758    0.000  176.773    0.000 {built-in method builtins.all}
               18600699  173.055    0.000  173.055    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                1001253  172.451    0.000  172.451    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               45382306   71.467    0.000  164.783    0.000 tensor.py:596(__hash__)
             1337153171  150.850    0.000  150.850    0.000 {method 'values' of 'collections.OrderedDict' objects}
              211819238  149.798    0.000  149.799    0.000 module.py:765(__getattr__)
        1099267016/1099267014  135.059    0.000  141.434    0.000 {built-in method builtins.len}
               45382196  118.304    0.000  118.304    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              262324136   91.612    0.000  113.298    0.000 layers.py:809(<genexpr>)
                7452449   36.818    0.000  109.875    0.000 __init__.py:28(_make_grads)
               29719577   24.115    0.000  107.520    0.000 flatten.py:39(forward)
               80188050   25.319    0.000  107.473    0.000 layers.py:799(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668389: <Diamonds1_0.5_NN_cpu_2_0> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_2_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:58:58 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:00 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:00 2021
Terminated at Thu May 20 08:54:02 2021
Results reported at Thu May 20 08:54:02 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35611.60 sec.
    Max Memory :                                 105 MB
    Average Memory :                             100.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16279.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35735 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

