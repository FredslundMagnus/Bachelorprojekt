
# Parameters

    Name :                      SuperCausal_convert4-2
    Main :                      CFagent
    Level :                     Levels.CausalSuper
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              2
    Topn :                      3
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      78831363429 function calls (78546839142 primitive calls) in 86119.11 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.114 86119.114 {built-in method builtins.exec}
                      1    4.241    4.241 86119.114 86119.114 <string>:1(<module>)
                      1  319.161  319.161 86114.873 86114.873 main.py:80(CFagent)
                9061494   34.298    0.000 27258.885    0.003 agent.py:29(learn)
                9061494  681.103    0.000 22747.499    0.003 learner.py:42(Qlearn)
                3020498   14.255    0.000 18716.068    0.006 game.py:42(step)
                3020498   20.166    0.000 17969.037    0.006 layers.py:827(step)
                3020498  965.930    0.000 14547.247    0.005 agent.py:212(counterfact)
                3020498  252.366    0.000 13240.609    0.004 layers.py:17(step)
              301782559  481.013    0.000 12959.774    0.000 layer.py:106(move)
        318301139/33778543 1319.562    0.000 11750.509    0.000 module.py:866(_call_impl)
               24717049   72.490    0.000 11029.078    0.000 network.py:28(forward)
               24717049  340.037    0.000 10795.598    0.000 container.py:117(forward)
                3020498  310.026    0.000 10526.560    0.003 agent.py:54(_learn)
              301782559 1333.177    0.000 9742.257    0.000 layers.py:844(check)
                3020498  307.018    0.000 9732.243    0.003 agent.py:204(_learn)
                9061494   79.449    0.000 9692.469    0.001 optimizer.py:84(wrapper)
                9061494   37.068    0.000 9325.758    0.001 grad_mode.py:24(decorate_context)
                9061494  266.823    0.000 9204.965    0.001 adam.py:55(step)
                9061494 1876.356    0.000 8646.242    0.001 _functional.py:53(adam)
               78229246 8465.723    0.000 8465.723    0.000 {built-in method tensor}
               71246261   41.002    0.000 8276.282    0.000 game.py:38(board)
                3020498   90.687    0.000 6946.054    0.002 agent.py:117(_learn)
                7823648  207.732    0.000 5671.525    0.001 agent.py:49(__call__)
                9061494   36.331    0.000 5641.533    0.001 tensor.py:195(backward)
                9061494   36.506    0.000 5603.709    0.001 __init__.py:68(backward)
                9061494 5363.011    0.001 5363.011    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3020498 4137.005    0.001 5130.316    0.002 replaybuffer.py:22(sample_data)
                3020498 3935.356    0.001 4894.825    0.002 replaybuffer.py:67(sample_data)
                3020499  412.473    0.000 4685.058    0.002 layers.py:793(update)
                3020498 2484.471    0.001 4663.479    0.002 replaybuffer.py:28(teleporter_save_data)
                3020498 2355.068    0.001 4540.216    0.002 agent.py:88(interveen)
               90614940 2412.856    0.000 4516.820    0.000 layer.py:175(NoRock_update)
               49434098  105.114    0.000 3897.328    0.000 conv.py:398(forward)
               49434098   66.930    0.000 3734.541    0.000 conv.py:390(_conv_forward)
               49434098 3667.611    0.000 3667.611    0.000 {built-in method conv2d}
               68110151  132.796    0.000 3121.302    0.000 linear.py:93(forward)
               68110151   55.782    0.000 2915.244    0.000 functional.py:1737(linear)
               68110151 2846.027    0.000 2846.027    0.000 {built-in method torch._C._nn.linear}
                1790911   38.063    0.000 2752.333    0.002 agent.py:176(choose_action)
                3020498 1671.681    0.001 2554.203    0.001 agent.py:67(modify)
            10956475447 1653.169    0.000 2380.569    0.000 enum.py:646(__hash__)
              301782559  527.984    0.000 2297.562    0.000 layers.py:838(isFree)
              301782559 1321.350    0.000 2104.777    0.000 layers.py:734(check)
              147405231 1938.110    0.000 1938.110    0.000 {built-in method clone}
              169147888 1787.478    0.000 1787.478    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2837698070 1447.240    0.000 1769.578    0.000 layer.py:103(isFree)
               92827200   80.127    0.000 1740.389    0.000 activation.py:713(forward)
               41049126 1699.816    0.000 1699.816    0.000 {built-in method cat}
               92827200   74.112    0.000 1660.262    0.000 functional.py:1364(leaky_relu)
               10844146   73.309    0.000 1574.596    0.000 agent.py:59(modify_board)
               92827200 1569.704    0.000 1569.704    0.000 {built-in method torch._C._nn.leaky_relu}
              169147888 1556.180    0.000 1556.180    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              301782559  960.509    0.000 1554.532    0.000 layers.py:700(check)
              301782559  961.819    0.000 1553.228    0.000 layers.py:717(check)
                3020498   52.624    0.000 1515.610    0.001 agent.py:172(__call__)
                3020498   51.825    0.000 1438.237    0.000 agent.py:112(__call__)
                9061494  217.132    0.000 1330.063    0.000 optimizer.py:189(zero_grad)
              306588644  291.464    0.000 1262.487    0.000 {built-in method builtins.any}
              832834995 1113.067    0.000 1113.067    0.000 layer.py:154(elements)
               10844146 1004.178    0.000 1004.178    0.000 {built-in method torch._C._nn.one_hot}
             3306024128  805.094    0.000  971.024    0.000 layers.py:809(<genexpr>)
               84573944  962.436    0.000  962.436    0.000 {method 'add' of 'torch._C._TensorBase' objects}
            10050793420  959.814    0.000  959.814    0.000 layer.py:99(positions)
                1502252   18.773    0.000  941.102    0.001 layers.py:849(restart)
                3020498  724.522    0.000  884.950    0.000 replaybuffer.py:73(CF_save_data)
               84573944  835.698    0.000  835.698    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1502252    8.670    0.000  811.122    0.001 level.py:8(__init__)
               84573944  807.852    0.000  807.852    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               84573944  795.155    0.000  795.155    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3020498   61.508    0.000  780.219    0.000 replaybuffer.py:18(stacker)
              301782559  491.238    0.000  774.002    0.000 layers.py:672(check)
                3020498   66.255    0.000  754.186    0.000 replaybuffer.py:63(stacker)
              301782559  470.185    0.000  749.728    0.000 layers.py:658(check)
              301782559  467.836    0.000  746.081    0.000 layers.py:686(check)
                1502252   26.231    0.000  729.637    0.000 levels.py:261(generate)
            10956509974  727.406    0.000  727.406    0.000 {built-in method builtins.hash}
        11168461331/11168461328  657.530    0.000  725.205    0.000 {built-in method builtins.len}
               12333325  112.478    0.000  676.393    0.000 level.py:41(notUsed)
                3020498  378.033    0.000  625.079    0.000 collector.py:46(collect)
               84573944  614.915    0.000  614.915    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7823648  214.523    0.000  591.902    0.000 exploration.py:53(softmaxer)
                1790911  464.546    0.000  550.848    0.000 agent.py:187(convert_values)
              161269875  494.782    0.000  494.782    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              592017692  390.299    0.000  482.855    0.000 tensor.py:906(grad)
                9061494   14.537    0.000  440.393    0.000 loss.py:527(forward)
                9061494   32.975    0.000  425.856    0.000 functional.py:2898(mse_loss)
                6040996  153.533    0.000  407.552    0.000 random.py:315(sample)
              302049900   66.819    0.000  401.269    0.000 {built-in method builtins.all}
              788380180  183.392    0.000  369.693    0.000 layers.py:799(<genexpr>)
              301782559  230.998    0.000  354.771    0.000 layers.py:646(check)
               12333325   10.816    0.000  323.980    0.000 level.py:38(elementsIn)
               90614940  303.152    0.000  303.152    0.000 layer.py:186(<listcomp>)
              301782559  198.721    0.000  298.507    0.000 layers.py:23(check)
               49434098   34.248    0.000  287.561    0.000 flatten.py:39(forward)
                9061494  282.002    0.000  282.002    0.000 {built-in method torch._C._nn.mse_loss}
             2837698070  273.990    0.000  273.990    0.000 layer.py:211(isBlocking)
               18122988  265.092    0.000  265.092    0.000 {built-in method sum}
                6040998  257.939    0.000  257.939    0.000 {built-in method nonzero}
               90614940  257.467    0.000  257.467    0.000 layer.py:187(<listcomp>)


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9672994: <SuperCausal_convert4_2> in cluster <dcc> Exited

Job <SuperCausal_convert4_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May 20 18:43:27 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May 21 18:38:56 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May 21 18:38:56 2021
Terminated at Sat May 22 18:34:34 2021
Results reported at Sat May 22 18:34:34 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   85896.64 sec.
    Max Memory :                                 8957 MB
    Average Memory :                             6074.12 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7427.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86139 sec.
    Turnaround time :                            172267 sec.

The output (if any) is above this job summary.

